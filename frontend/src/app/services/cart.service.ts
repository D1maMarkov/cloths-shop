import { HttpClient, HttpHeaders, HttpErrorResponse } from "@angular/common/http";
import { Observable, catchError, throwError, BehaviorSubject } from 'rxjs';
import { GlobalSettingsService } from "./global-settings.service";
import { AuthService } from 'src/app/services/auth.service';
import { MatSnackBar } from "@angular/material/snack-bar";
import { TypeCartProduct } from 'src/app/models/product';
import { ErrorService } from "./error.service";
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class CartService{
  host: string;
  opened: boolean = true;

  len: number = 0;
  products = new BehaviorSubject<TypeCartProduct[]>([]);

  price: number;
  checkClick: boolean = true;

  httpOptions = { 
    withCredentials: true,
    headers: new HttpHeaders({
      'accept': 'application/json',
      'Content-Type': 'application/json',
  })
  };

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

  increment(product: TypeCartProduct): void{
    product.quantity++;
    this.price += Number(product.price);
    this.len++
    this.addInSession(product);
  }

  decrement(product: TypeCartProduct): void{
    product.quantity--;
    this.price -= Number(product.price);
    this.len--;
    this.lowQuantityInSession(product);

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
    this.clearSession();
    this.http.get(this.host + '/clear', this.httpOptions).subscribe();
  }

  clearSession(): void{
    this.http.get(this.host + '/clear', this.httpOptions).subscribe();
  }

  constructor(
    private http: HttpClient,
    private errorService: ErrorService,
    private global: GlobalSettingsService,
    private route: Router,
    private authService: AuthService,
    private snackBar: MatSnackBar,
  ){
    this.host = this.global.host + 'cart'
    this.getCart().subscribe(products => {
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

  getCart(): Observable<TypeCartProduct[]>{
    return this.http.get<TypeCartProduct[]>(this.host + '/get', this.httpOptions).pipe(
      catchError(this.errorHandler.bind(this))
    )
  }

  private errorHandler(error: HttpErrorResponse){
    this.errorService.handle(error.message)
    return throwError(() => error.message)
  }

  addInSession(product: TypeCartProduct){
    this.http.post(this.host + '/add', product, this.httpOptions).subscribe()
  }

  lowQuantityInSession(product: TypeCartProduct){
    this.http.post(this.host + `/low-quantity`, product, this.httpOptions).subscribe()
  }

  addProduct(cartProduct: TypeCartProduct){
    const products = this.products.getValue()
    let inCart = false;
    for (let product of products){
      if (product.id === cartProduct.id && product.size === cartProduct.size){
        product.quantity++;
        inCart = true;
        break;
      }
    }
  
    if (!inCart){
      products.push(cartProduct);
    }

    this.products.next(products);
    this.addInSession(cartProduct);
  }

  isInCart(product: TypeCartProduct): boolean{
    let inCart = false;
    this.products.getValue().forEach((cartProduct: TypeCartProduct) => {
      if (cartProduct.id === product.id && cartProduct.size === product.size){
        inCart = true;
      }
    })

    return inCart;
  }

  getProduct(product: TypeCartProduct){
    let result: TypeCartProduct = this.products.getValue()[0];

    this.products.getValue().forEach((cartProduct: TypeCartProduct) => {
      if (product.id === cartProduct.id && product.size === cartProduct.size){
        result = cartProduct;
      }
    })

    return result;
  }
}