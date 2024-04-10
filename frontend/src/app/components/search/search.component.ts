import { Component, OnInit } from '@angular/core';
import { ProductsService } from 'src/app/services/products.service';
import { SearchService } from 'src/app/services/search.service';
import { fadeInOutTopnav } from 'src/app/animations/fade-in-out-topnav.animation';
import { Observable } from 'rxjs';
import { ICatalogProduct } from 'src/app/models/product';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss'],
  animations: [fadeInOutTopnav]
})
export class SearchComponent implements OnInit {
  history: string[] = [];

  nothingFound: boolean = false;
  products$: Observable<ICatalogProduct[]> = this.productService.getSearched("");

  search: string = "";

  alsoSearch: string[] = [
    "stone island",
    "givenchy",
    "chrome hearts",
    "rick owens pink"
  ];

  constructor(
    public searchService: SearchService,
    private productService: ProductsService
  ) {

  }

  getHistorySearch(): string[]{
    const raw = localStorage.getItem("history");

    let history: string[] = [];
    if (raw != null){
      history = JSON.parse(raw);
    }

    return history
  }

  getSearchedProducts(search: string): void{
    this.search = search
    this.products$ = this.productService.getSearched(search);
    this.addToHistorySearch(search);
  }

  addToHistorySearch(newValue: string): void{
    let history = this.getHistorySearch();

    history = history.filter((option: string) => option != newValue);

    history.unshift(newValue);

    this.history = history;
    localStorage.setItem("history", JSON.stringify(history));
  }

  deleteFromHistorySearch(value: string): void{
    let history = this.getHistorySearch();

    history = history.filter((option: string) => option != value);

    this.history = history;
    localStorage.setItem("history", JSON.stringify(history));
  }

  ngOnInit(): void {
    this.history = this.getHistorySearch();
  }
}
