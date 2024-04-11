import { BehaviorSubject, Observable, tap } from 'rxjs';
import { TypeDataField, TypePriceRange } from '../models/filter';
import { DataService } from './data.service';
import { Injectable } from '@angular/core';
import { genders } from "../data/filter";

@Injectable({
  providedIn: 'root'
})
export class FilterService{
  genders: TypeDataField[] = genders;
  colors: TypeDataField[];
  sizes: TypeDataField[];
  brands: TypeDataField[];
  categories: TypeDataField[];

  genderFilters$ = new BehaviorSubject<string[]>([]);
  categoryFilters$ = new BehaviorSubject<string[]>([]);
  colorFilters$ = new BehaviorSubject<string[]>([]);
  sizeFilters$ = new BehaviorSubject<string[]>([]);
  brandFilters$ = new BehaviorSubject<string[]>([]);
  basicCategory$ = new BehaviorSubject<string>("cloths");

  price$ = new BehaviorSubject<number>(0);
  quantity$ = new BehaviorSubject<number>(24);
  pageIndex$ = new BehaviorSubject<number>(0);
  orderBy$ = new BehaviorSubject<string>("-price");
  priceRange$ = new Observable<TypePriceRange>;

  constructor(
    private data: DataService
  ){
    this.data.brands$.subscribe(brands => {
      this.brands = brands;
    })
    this.data.sizes$.subscribe(sizes => {
      this.sizes = sizes;
    })
    this.data.categories$.subscribe(categories => {
      this.categories = categories;
    })
    this.data.colors$.subscribe(colors => {
      this.colors = colors;
    })
    this.priceRange$ = this.data.getPriceRange().pipe(
      tap((range) => {
        this.price$.next(range.max_price)
      })
    );
  }

  updatePageIndex(value: number, top?: boolean): void{
    if (top){
      window.scrollTo(0, 0);
    }
    this.pageIndex$.next(value);
  }

  updatePageIndexIncrement(): void{
    this.updatePageIndex(this.pageIndex$.getValue() + 1, true);
  }

  updateGender(value: string): void{
    this.updatePageIndex(0);
    if (this.genderFilters$.getValue().includes(value)){
      this.genderFilters$.next([...this.genderFilters$.getValue().filter((gender: string) => gender != value)]);
    }
    else{
      this.genderFilters$.next([...this.genderFilters$.getValue(), value]);
    }
  }

  updateCategory(value: string): void{
    this.updatePageIndex(0);
    if (this.categoryFilters$.getValue().includes(value)){
      this.categoryFilters$.next([...this.categoryFilters$.getValue().filter((category: string) => category != value)]);
    }
    else{
      this.categoryFilters$.next([...this.categoryFilters$.getValue(), value]);
    }
  }

  updateColor(value: string): void{
    this.updatePageIndex(0);
    if (this.colorFilters$.getValue().includes(value)){
      this.colorFilters$.next([...this.colorFilters$.getValue().filter((color: string) => color != value)]);
    }
    else{
      this.colorFilters$.next([...this.colorFilters$.getValue(), value]);
    }
  }

  updateSizes(value: string): void{
    this.updatePageIndex(0);
    if (this.sizeFilters$.getValue().includes(value)){
      this.sizeFilters$.next([...this.sizeFilters$.getValue().filter((size: string) => size != value)]);
    }
    else{
      this.sizeFilters$.next([...this.sizeFilters$.getValue(), value]);
    }
  }

  updateBrand(value: string): void{
    this.updatePageIndex(0);
    if (Object.keys(this.brands).length > 1){
      if (this.brandFilters$.getValue().includes(value)){
        this.brandFilters$.next([...this.brandFilters$.getValue().filter((brand: string) => brand != value)]);
      }
      else{
        this.brandFilters$.next([...this.brandFilters$.getValue(), value]);
      }
    }
  }

  updateQuantity(value: Event): void{
    this.quantity$.next(Number((value.target as HTMLInputElement).value));
  }

  updateOrderBy(value: Event): void{
    this.orderBy$.next((value.target as HTMLInputElement).value);
  }

  reset(): void{
    this.brandFilters$.next([]);
    this.genderFilters$.next([]);
    this.sizeFilters$.next([]);
    this.categoryFilters$.next([]);
    this.colorFilters$.next([]);
    this.price$.next(5000);

    const checkboxes: HTMLInputElement[] = Array.from(document.querySelectorAll('input[type=checkbox]'));

    checkboxes.forEach(checkbox => {
      checkbox.checked = false;
    })
  }

  globalReset(): void{
    this.reset();
    this.genders = genders;
    this.data.getCategories();
    this.data.getColors();
    this.data.getSizes();
    this.data.getBrands();
    this.basicCategory$.next("cloths");
  }

  setDefaultGender(gender: TypeDataField): void{
    this.genders = [gender];
    this.genderFilters$.next([gender.name]);
  }

  setDefaultMainCategory(category: string): void{
    this.basicCategory$.next(category);
  }
}
