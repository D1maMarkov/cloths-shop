import { fadeInOutTopnav } from 'src/app/animations/fade-in-out-topnav.animation';
import { Component, OnInit, HostListener, ElementRef } from '@angular/core';
import { fadeIn } from 'src/app/animations/fade-in.animation';
import { CartService } from 'src/app/services/cart.service';
import { ICartProduct } from 'src/app/models/product';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss'],
  animations: [fadeIn, fadeInOutTopnav]
})
export class CartComponent implements OnInit {
  products: ICartProduct[] = [];
  deleteWarning: boolean = false;
  readyToChangeDelete: boolean = false;
  checkClick: boolean = true;

  len: number;
  price: number;

  constructor(
    private element: ElementRef,
    public cartService: CartService,
    private route: Router,
  ) {
    this.cartService.products.subscribe(products => {
      this.products = products;
      this.len = this.cartService.len;
      this.price = this.cartService.price;
    })
  }

  delete(): void{
    this.readyToChangeDelete = true;
    this.cartService.clear();
  }

  exit(): void{
    this.route.navigate(['catalog/new']);
    this.cartService.opened = false;
  }

  ngOnInit(): void {
  }

  decrement(product: ICartProduct): void{
    this.cartService.decrement(product);
  }

  @HostListener('document:click', ['$event'])
  onClick(event: MouseEvent) {
    if (this.checkClick){
      if (this.readyToChangeDelete){
        this.deleteWarning = true;
        this.readyToChangeDelete = false
      }
      else if (!this.element.nativeElement.contains(event.target)) {
        if (this.cartService.opened === true){
          const element = document.getElementById('cart-icon');

          if (event.target === element) {
            this.cartService.opened = true;
          }
          else{
            this.cartService.opened = false;
          }
        }
      }
    }
    else{
      this.checkClick = true;
    }
  }
}
