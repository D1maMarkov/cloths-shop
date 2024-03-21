import { TopnavRedirectService } from 'src/app/services/topnav-redirect.service';
import { ProductsService } from 'src/app/services/products.service';
import { FilterService } from 'src/app/services/filter.service';
import { fadeIn } from 'src/app/animations/fade-in.animation';
import { Title } from '@angular/platform-browser';
import { IProduct } from 'src/app/models/product';
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss'],
  animations: [fadeIn]
})
export class MainPageComponent{
  popularProducts$: Observable<IProduct[]>;
  newArrivals$: Observable<IProduct[]>;

  constructor(
    public filter: FilterService, 
    private titleService: Title, 
    public topnavService: TopnavRedirectService,
    public route: Router,
    private productService: ProductsService
  ) { 
    this.titleService.setTitle("Магазин брендовой одежды | 1000 и 1 рик овенс");
    this.popularProducts$ =  this.productService.getPopularProducts()
    this.newArrivals$ =  this.productService.getNewArrivals()
  }
}
