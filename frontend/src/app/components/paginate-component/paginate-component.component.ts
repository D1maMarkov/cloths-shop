import { flyInOutLeft } from 'src/app/animations/fly-in-out-left.animation';
import { flyInOut } from 'src/app/animations/fly-in-out.animation';
import { Component, OnInit, Input } from '@angular/core';
import { TypeBaseProduct } from 'src/app/models/product';

@Component({
  selector: 'app-paginate-component',
  templateUrl: './paginate-component.component.html',
  styleUrls: ['./paginate-component.component.scss'],
  animations: [flyInOut, flyInOutLeft]
})
export class PaginateComponent implements OnInit {
  index: number = 0;
  totalLength: number;
  right: boolean = false;
  productsPerPage: number = 4;

  @Input() objects: TypeBaseProduct[];
  @Input() title: string;

  increment(): void{
    this.index++;
    this.right = true;
  }

  decrement(): void{
    this.index--;
    this.right = false;
  }

  ngOnInit(): void {
    this.totalLength = Math.ceil(this.objects.length / this.productsPerPage);
  }
}
