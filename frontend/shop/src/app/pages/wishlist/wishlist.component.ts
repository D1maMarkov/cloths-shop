import { Component, OnInit } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { IProduct } from 'src/app/models/product';
import { FavsService } from 'src/app/services/favs.service';
import { fadeIn } from 'src/app/animations/fade-in.animation';

@Component({
  selector: 'app-wishlist',
  templateUrl: './wishlist.component.html',
  styleUrls: ['./wishlist.component.scss'],
  animations: [fadeIn]
})
export class WishlistComponent implements OnInit {
  products = new BehaviorSubject<IProduct[]>([]);

  constructor(
    private favsService: FavsService
  ){
    this.favsService.getFavs().subscribe(products => {
      this.products.next(products);
    })
  }

  ngOnInit(): void {
  }
}
