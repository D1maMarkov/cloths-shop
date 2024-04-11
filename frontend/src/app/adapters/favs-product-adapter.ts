import { Injectable } from '@angular/core';
import { ICatalogProduct, IProduct } from '../models/product';

@Injectable({
  providedIn: 'root'
})
export class FavsProductAdapter{
    getProduct(product: IProduct): ICatalogProduct{
        return {
            id: product.id,
            image: product.images[0],
            name: product.name,
            description: product.description,
            price: product.price,
            sizes: product.sizes
        }
    }
}
