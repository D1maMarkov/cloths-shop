import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {

  information: string[] = ['Контакты', 'Магазины', 'Блог', 'Вакансии'];
  support: string[] = ['Помощь покупателю', 'Доставка и оплата', 'Возврат', 'Программа лояльности', 'Партнёры'];
  phones: string[] = ['+79505163534', '+74429489248'];
  
  constructor() { }

  ngOnInit(): void {
  }

}
