import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class IsVisibleImageService {
  visibleImageId$ = new Subject<number>;

  constructor() { }
}
