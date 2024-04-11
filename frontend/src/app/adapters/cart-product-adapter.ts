import { Injectable } from '@angular/core';
import { ICartProduct, IProduct } from '../models/product';

@Injectable({
  providedIn: 'root'
})
export class CartProductAdapter{
    getProduct(product: IProduct, chosedSize: string): ICartProduct{
        return {
            id: product.id,
            name: product.name,
            description: product.description,
            price: product.price,
            size: chosedSize,
            quantity: 0,
            image: product.images[0]
        };
    }
}
