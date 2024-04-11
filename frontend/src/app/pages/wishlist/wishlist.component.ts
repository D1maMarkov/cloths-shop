import { Component } from '@angular/core';
import { ICatalogProduct } from 'src/app/models/product';
import { fadeIn } from 'src/app/animations/fade-in.animation';
import { HttpFavsService } from 'src/app/http-services/http-favs-service.service';

@Component({
  selector: 'app-wishlist',
  templateUrl: './wishlist.component.html',
  styleUrls: ['./wishlist.component.scss'],
  animations: [fadeIn]
})
export class WishlistComponent {
  products: ICatalogProduct[] = [];

  constructor(
    private httpFavsService: HttpFavsService
  ){
    this.httpFavsService.getFavs().subscribe(products => {
      this.products = products;
    })
  }
}
