import { SearchService } from './services/search.service';
import { CartService } from './services/cart.service';
import { Component, OnInit } from '@angular/core';
import { NavigationEnd } from '@angular/router';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})

export class AppComponent implements OnInit{
  constructor(
    private router: Router,
    private cartService: CartService,
    private searchService: SearchService
  ) {

  }

  ngOnInit() {
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        this.cartService.opened = false;
        window.scrollTo(0, 0);
        this.searchService.close();
      }
    });
  }
}
