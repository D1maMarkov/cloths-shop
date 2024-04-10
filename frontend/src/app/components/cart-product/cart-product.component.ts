import { fadeInOut } from 'src/app/animations/fade-in-out.animation';
import { CartService } from 'src/app/services/cart.service';
import { Component, Input, OnInit } from '@angular/core';
import { ICartProduct } from 'src/app/models/product';

@Component({
  selector: 'app-cart-product',
  templateUrl: './cart-product.component.html',
  styleUrls: ['./cart-product.component.scss'],
  animations: [fadeInOut]
})
export class CartProductComponent implements OnInit {
  @Input() product: ICartProduct;

  constructor(
    public cartService: CartService,
  ){

  }

  ngOnInit(): void {
  }
}
