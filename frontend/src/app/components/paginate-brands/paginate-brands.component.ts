import { TopnavRedirectService } from 'src/app/services/topnav-redirect.service';
import { PaginateBrandsService } from 'src/app/http-services/paginate-brands.service';
import { flyInOutLeft } from 'src/app/animations/fly-in-out-left.animation';
import { flyInOut } from 'src/app/animations/fly-in-out.animation';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-paginate-brands',
  templateUrl: './paginate-brands.component.html',
  styleUrls: ['./paginate-brands.component.scss'],
  animations: [flyInOut, flyInOutLeft]
})
export class PaginateBrands{
  index: number = 0;
  totalLength: number;
  right: boolean = false;
  productsPerPage: number = 4;

  @Input() title: string;

  increment(): void{
    this.index++;
    this.right = true;
  }

  decrement(): void{
    this.index--;
    this.right = false;
  }

  constructor(
    public TopnavService: TopnavRedirectService,
    public BrandsService: PaginateBrandsService
  ){
    this.BrandsService.brands$.subscribe(brands => {
      this.totalLength = Math.ceil(brands.length / this.productsPerPage);
    })
  }
}
