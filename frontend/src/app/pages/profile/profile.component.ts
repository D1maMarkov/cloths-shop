import { OrdersService } from 'src/app/services/orders.service';
import { FavsService } from 'src/app/services/favs.service';
import { AuthService } from 'src/app/services/auth.service';
import { Observable } from 'rxjs';
import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { TypeOrder } from 'src/app/models/order';
import { Router } from '@angular/router';
import { UserInfoType } from 'src/app/models/auth';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  userInfo: UserInfoType;
  orders$: Observable<TypeOrder[]>;

  constructor(
    private titleService: Title,
    private authService: AuthService,
    public route: Router,
    public favsService: FavsService,
    private ordersSerivice: OrdersService,
  ) {
    this.titleService.setTitle("Мой профиль");
    this.getUserInfo();
    this.orders$ = this.ordersSerivice.getOrders();
  }

  async getUserInfo(){
    const userInfo = await this.authService.getUserInfo();
    if (userInfo){
      this.userInfo = userInfo
    }
  }

  logout(): void{
    this.authService.logout();
    this.route.navigate(["/"])
  }

  ngOnInit(): void {
  }

}
