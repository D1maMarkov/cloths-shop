import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SearchService {
  opened: boolean = false;

  visible(): void{
    this.opened = !this.opened;
  }

  close(): void{
    this.opened = false;
  }
}
