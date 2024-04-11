import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-underlined-text',
  templateUrl: './underlined-text.component.html',
  styleUrls: ['./underlined-text.component.scss']
})
export class UnderlinedTextComponent{
  @Input() text: string;
  @Input() color?: string;

  constructor() { }
}
