import { BehaviorSubject } from 'rxjs';
import { Injectable } from '@angular/core';
import { IProduct, ICatalogProduct } from '../models/product';
import { HttpFavsService } from '../http-services/http-favs-service.service';
import { FavsProductAdapter } from '../adapters/favs-product-adapter';

@Injectable({
  providedIn: 'root'
})
export class FavsService{
  len: number = 0;
  products = new BehaviorSubject<ICatalogProduct[]>([]);

  constructor(
    private httpFavsService: HttpFavsService,
    private favsProductAdapter: FavsProductAdapter
  ){
    this.httpFavsService.getFavs().subscribe(products => {
      this.products.next([...products]);
    })

    this.products.subscribe(products => {
      this.len = products.length;
    })
  }

  addProduct(product: IProduct){
    const favsProduct: ICatalogProduct = this.favsProductAdapter.getProduct(product);

    const products = this.products.getValue()
    this.products.next([...products, favsProduct]);
    this.httpFavsService.addInSession(favsProduct);
  }

  removeProduct(id: number){
    this.products.next([...this.products.getValue().filter(product => product.id !== id)]);
    this.httpFavsService.removeFromSession(id);
  }

  isInFavs(id: number){
    let isIn = false;
    this.products.getValue().forEach(product => {
      if (product.id === id){
        isIn = true;
      }
    })

    return isIn;
  }
}
