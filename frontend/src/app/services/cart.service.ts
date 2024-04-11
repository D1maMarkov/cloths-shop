import { BehaviorSubject } from 'rxjs';
import { AuthService } from 'src/app/http-services/auth.service';
import { MatSnackBar } from "@angular/material/snack-bar";
import { ICartProduct } from 'src/app/models/product';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpCartService } from "../http-services/http-cart-service.service";

@Injectable({
  providedIn: 'root'
})
export class CartService{
  opened: boolean = true;

  len: number = 0;
  products = new BehaviorSubject<ICartProduct[]>([]);

  price: number;
  checkClick: boolean = true;

  async openSnackBar(){
    const isAuth = await this.authService.isAuth();
    if (isAuth){
      this.route.navigate(["order"])
    }
    else{
      let snack = this.snackBar.open('Для оформления заказа нужно войти в аккаунт', 'Войти', {
        duration: 3000,
        verticalPosition: 'bottom',
        horizontalPosition: 'left',
        panelClass: 'snack'
      });

      snack.onAction().subscribe(() => {
        this.route.navigate(["login"]);
      });
    }
  }

  increment(product: ICartProduct): void{
    product.quantity++;
    this.price += Number(product.price);
    this.len++
    this.httpCartService.addInSession(product);
  }

  decrement(product: ICartProduct): void{
    product.quantity--;
    this.price -= Number(product.price);
    this.len--;
    this.httpCartService.lowQuantityInSession(product);

    if (product.quantity === 0){
      const productId = product.id;
      const productSize = product.size;
      this.checkClick = false;
      this.products.next([...this.products.getValue().filter(product => !(product.id === productId && product.size === productSize))])
    }
  }

  clear(): void{
    this.len = 0;
    this.products.next([]);
    this.httpCartService.clearSession();
  }

  constructor(
    private httpCartService: HttpCartService,
    private route: Router,
    private authService: AuthService,
    private snackBar: MatSnackBar,
  ){
    this.httpCartService.getCart().subscribe(products => {
      this.products.next([...products]);
    })

    this.products.subscribe(products => {
      let curPrice = 0;
      let curLen = 0;

      products.forEach(product => {
        curPrice += Number(product.price) * product.quantity;
        curLen += Number(product.quantity);
      })

      this.price = curPrice;
      this.len = curLen;
    })
  }

  addProduct(cartProduct: ICartProduct){
    const products = this.products.getValue()
    for (let product of products){
      if (product.id === cartProduct.id && product.size === cartProduct.size){
        product.quantity++;
        break;
      }
    }

    if (!this.isInCart(cartProduct)){
      products.push(cartProduct);
    }

    this.products.next(products);
    this.httpCartService.addInSession(cartProduct);
  }

  isInCart(product: ICartProduct): boolean{
    let inCart = false;
    this.products.getValue().forEach((cartProduct: ICartProduct) => {
      if (cartProduct.id === product.id && cartProduct.size === product.size){
        inCart = true;
      }
    })

    return inCart;
  }

  getProduct(product: ICartProduct){
    let result: ICartProduct = this.products.getValue()[0];

    this.products.getValue().forEach((cartProduct: ICartProduct) => {
      if (product.id === cartProduct.id && product.size === cartProduct.size){
        result = cartProduct;
      }
    })

    return result;
  }
}
