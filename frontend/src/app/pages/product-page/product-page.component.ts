import { IsVisibleImageService } from 'src/app/services/is-visible-image.service';
import { ProductsService } from 'src/app/http-services/products.service';
import { IProduct, ICatalogProduct } from 'src/app/models/product';
import { SearchService } from 'src/app/services/search.service';
import { TypeDataField } from 'src/app/models/filter';
import { BehaviorSubject, Observable } from 'rxjs';
import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: 'app-product-page',
  templateUrl: './product-page.component.html',
  styleUrls: ['./product-page.component.scss'],
})
export class ProductPageComponent implements OnInit {
  defaultRefs: TypeDataField[] = [{viewed_name: "Новинки", name: 'unisex'}];

  refs = new BehaviorSubject<TypeDataField[]>([]);

  product: IProduct;
  products$: Observable<ICatalogProduct[]>;

  visibleImageId: number;

  constructor(
    private productsService: ProductsService,
    private route: ActivatedRoute,
    private visibleService: IsVisibleImageService,
    private titleService: Title,
    private searchService: SearchService,
  ){
    this.searchService.close();
    this.products$ = this.productsService.getSearched("");
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const id = params['id'];

      this.productsService.getProduct(id).subscribe(product => {
        this.product = product;

        this.refs.next([...this.defaultRefs,
          {name: product.category.name, viewed_name: product.category.viewed_name},
          {name: product.name, viewed_name: product.name}]
        );

        this.titleService.setTitle(product.name);
      })
    });

    this.visibleService.visibleImageId$.subscribe(id => {
      this.visibleImageId = id;
    })
  }
}
