import { Location } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-simple-topnav',
  templateUrl: './simple-topnav.component.html',
  styleUrls: ['./simple-topnav.component.scss']
})
export class SimpleTopnavComponent{

  constructor(
    private location: Location
  ) {

  }

  back() {
    this.location.back();
  }
}
