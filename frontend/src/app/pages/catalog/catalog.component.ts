import { Component, OnInit } from '@angular/core';
import { TypeBaseProduct } from 'src/app/models/product';
import { ProductsService } from 'src/app/services/products.service';
import { Observable, tap } from 'rxjs';
import { FilterService } from 'src/app/services/filter.service';
import { TopnavFiltersService } from 'src/app/services/topnav-filters.service';
import { Title } from '@angular/platform-browser';
import { ActivatedRoute } from '@angular/router';
import { TopnavRedirectService } from 'src/app/services/topnav-redirect.service';
import { fadeIn } from 'src/app/animations/fade-in.animation';
import { DataService } from 'src/app/services/data.service';
import { TypeDataFilter } from 'src/app/models/filter';


@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styleUrls: ['./catalog.component.scss'],
  animations: [fadeIn]
})
export class CatalogComponent implements OnInit {
  products$: Observable<TypeBaseProduct[]>;
  loading : boolean = true;
  totalCount: number;
  brands: TypeDataFilter[];

  constructor(
    private productsService: ProductsService,
    public filter: FilterService,
    public topnavFilterService: TopnavFiltersService,
    private titleService: Title,
    private activatedRoute: ActivatedRoute,
    private TopnavService: TopnavRedirectService,
    private data: DataService
  ){
    this.topnavFilterService.refs$.subscribe(refs => {
      if (refs[0] !== undefined){
        this.titleService.setTitle(refs[0].viewed_name);
      }
    })

    this.data.brands$.subscribe(brands => {
      this.brands = brands;
    })

    this.activatedRoute.params.subscribe((params) => {
      const label = params["label"];

      if (label === "zhenskoe"){
        this.filter.setDefaultGender('female', 'Женский');
        this.topnavFilterService.refs$.next([{viewed_name: "Женская одежда и обувь", name: 'female'}]);
      }
      else if (label === "muzhskoe"){
        this.filter.setDefaultGender('male', 'Мужской');
        this.topnavFilterService.refs$.next([{viewed_name: "Мужская одежда и обувь", name: 'male'}]);
      }
      else if (label === "accessories"){
        this.filter.setDefaultMainCategory("accessories");
        this.topnavFilterService.refs$.next([{viewed_name: "Аксессуары", name: 'accessories'}]);
      }
      else if (label !== "new" && label !== "brands"){
        for (let brand of this.brands){
          if (brand.name.toLowerCase() === label.toLowerCase()){
            this.TopnavService.defaultFilter({brand: label})
            this.topnavFilterService.refs$.next([{viewed_name: brand.name, name: brand.name}]);
          }
        }
      }
      else{
        this.topnavFilterService.refs$.next([
          {
            viewed_name: "Одежда для женщин и мужчин",
            name: 'unisex'
          }]);
      }
    });
  }

  filterProducts(){
    this.loading = true;
    this.products$ = this.productsService.getFiltered().pipe(
      tap((products) => {
        this.loading = false;
        this.totalCount = products.length;
      })
    )
  }

  ngOnInit(): void {
    this.filter.orderBy$.subscribe(() => this.filterProducts());
    this.filter.pageIndex$.subscribe(() => this.filterProducts());
    this.filter.genderFilters$.subscribe(() => this.filterProducts());
    this.filter.categoryFilters$.subscribe(() => this.filterProducts());
    this.filter.brandFilters$.subscribe(() => this.filterProducts());
    this.filter.colorFilters$.subscribe(() => this.filterProducts());
    this.filter.sizeFilters$.subscribe(() => this.filterProducts());
    this.filter.price$.subscribe(() => this.filterProducts());
    this.filter.basicCategory$.subscribe(() => this.filterProducts());
    this.filter.quantity$.subscribe(() => {this.filterProducts(); this.filter.pageIndex$.next(0)});
  }
}
