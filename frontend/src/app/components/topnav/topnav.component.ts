import { Component } from '@angular/core';
import { FilterService } from 'src/app/services/filter.service';
import { Router } from "@angular/router";
import { novelsImages, brandsImages, male, female, accessories, labels } from 'src/app/data/topnav';
import { TopnavRedirectService } from 'src/app/services/topnav-redirect.service';
import { CartService } from 'src/app/services/cart.service';
import { SearchService } from 'src/app/services/search.service';
import { fadeIn } from 'src/app/animations/fade-in.animation';
import { DataService } from 'src/app/services/data.service';
import { TypeDataField } from 'src/app/models/filter';
import { FavsService } from 'src/app/services/favs.service';
import { AuthService } from 'src/app/http-services/auth.service';

@Component({
  selector: 'app-topnav',
  templateUrl: './topnav.component.html',
  styleUrls: ['./topnav.component.scss'],
  animations: [fadeIn]
})
export class TopnavComponent {
  brands: TypeDataField[];
  categories: TypeDataField[];
  accessoriesCategories: TypeDataField[];
  labels = labels;
  allBrandsList: TypeDataField[];
  images = [novelsImages, brandsImages, male, female, accessories];

  searchOpened: boolean = false;
  isAuth: boolean = false;
  username: string = '';

  constructor(
    public filter: FilterService,
    public TopnavService: TopnavRedirectService,
    public route: Router,
    public cartService: CartService,
    public favsService: FavsService,
    public searchService: SearchService,
    private data: DataService,
    private authService: AuthService
  ) {
    this.data.brands$.subscribe(brands => {
      this.brands = brands;
      this.allBrandsList = brands;
    })
    this.data.categories$.subscribe(categories => {
      this.categories = categories;
    })
    this.data.accessoriesCategories$.subscribe(categories => {
      this.accessoriesCategories = categories;
    })
    this.getUser();
  }

  async goToProfile(){
    const isAuth = await this.authService.isAuth();
    if (isAuth){
      this.route.navigate(["/profile"])
    }
    else {
      this.route.navigate(["/login"])
    };
  }

  async getUser(){
    const isAuth = await this.authService.isAuth()
    if (isAuth){
      const userInfo = await this.authService.getUserInfo();
      if (userInfo){
        this.username = userInfo.username[0];
      }
      this.isAuth = true;
    }
    else{
      this.isAuth = false;
    }
  }
}
