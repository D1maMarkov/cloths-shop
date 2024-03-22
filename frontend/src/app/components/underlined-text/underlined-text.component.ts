import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-underlined-text',
  templateUrl: './underlined-text.component.html',
  styleUrls: ['./underlined-text.component.scss']
})
export class UnderlinedTextComponent implements OnInit {
  @Input() text: string;
  @Input() color?: string;

  constructor() { }

  ngOnInit(): void {
  }

}
