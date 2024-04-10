import { GlobalSettingsService } from 'src/app/services/global-settings.service';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { flyInOut } from 'src/app/animations/fly-in-out.animation';
import { CartService } from 'src/app/services/cart.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject } from 'rxjs';
import { OrdersService } from 'src/app/services/orders.service';
import { ICartProduct } from 'src/app/models/product';
import { TypeCreateOrder } from 'src/app/models/order';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.scss'],
  animations: [flyInOut]
})
export class OrderComponent implements OnInit {
  products: ICartProduct[] = [];
  host: string;
  formInd = 0;

  deliveryPrice = new BehaviorSubject<number>(10);
  deliveryMethods = ['на почту', 'курьером'];
  paymentMethods = ['наличными', 'картой'];
  chosedDeliveryMethod = new BehaviorSubject<string>(this.deliveryMethods[0]);
  chosedPaymentMethod = new BehaviorSubject<string>(this.paymentMethods[0]);

  firstForm = new FormGroup({
    firstName: new FormControl('', [Validators.required]),
    secondName: new FormControl('', [Validators.required]),
    phone: new FormControl('', [Validators.required, Validators.pattern(/^79\d{9}$/)]),
    adress: new FormControl('', [Validators.required]),
  });

  onSubmitFirstForm(): void{
    if (this.firstForm.valid) {
      this.formInd = 1;
    }
  }

  place(): void{
    const data: TypeCreateOrder = {
      name: this.firstForm.get('firstName')?.value,
      secondname: this.firstForm.get('secondName')?.value,
      delivery: this.chosedDeliveryMethod.getValue(),
      payment: this.chosedPaymentMethod.getValue(),
      adress: this.firstForm.get('adress')?.value,
      phone: this.firstForm.get('phone')?.value,
    }

    this.ordersService.place(data);
    this.formInd = 2;

    this.cartService.clearSession();
  }

  exit(): void{
    this.cartService.clear();
    this.router.navigate(["catalog/new"]);
  }

  changeDeliveryMethod(event: Event){
    const value = (event.target as HTMLInputElement).value;
    if (value == "курьером"){
      this.deliveryPrice.next(10);
    }
    else{
      this.deliveryPrice.next(0);
    }
    this.chosedDeliveryMethod.next(value)
  }

  changePaymentMethod(event: Event){
    this.chosedPaymentMethod.next((event.target as HTMLInputElement).value)
  }

  back(): void{
    this.formInd = 1;
  }

  constructor(
    public cartService: CartService,
    private global: GlobalSettingsService,
    private router: Router,
    private ordersService: OrdersService,
  ) {
    this.host = this.global.host;
    this.cartService.products.subscribe(products => {
      this.products = products;
    })
  }

  ngOnInit(): void {
  }
}
