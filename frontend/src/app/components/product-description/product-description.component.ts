import { Component, Input, OnInit } from '@angular/core';
import { IProduct, ICartProduct, ICatalogProduct } from 'src/app/models/product';
import { CartService } from 'src/app/services/cart.service';
import { FavsService } from 'src/app/services/favs.service';
import { BehaviorSubject, Observable } from 'rxjs';
import { CartProductAdapter } from 'src/app/adapters/cart-product-adapter';
import { ProductsService } from 'src/app/http-services/products.service';
import { fadeIn } from 'src/app/animations/fade-in.animation';

@Component({
  selector: 'app-product-description',
  templateUrl: './product-description.component.html',
  styleUrls: ['./product-description.component.scss'],
  animations: [fadeIn]
})
export class ProductDescriptionComponent implements OnInit{
  @Input() product: IProduct;
  constructor(
    public cartService: CartService,
    public favsService: FavsService,
    private productCartAdapter: CartProductAdapter,
    private productsService: ProductsService
  ) { }

  colors$: Observable<ICatalogProduct[]>;

  cartProduct: ICartProduct;
  chosedSize = new BehaviorSubject<string>('');

  changeSize(event: Event): void{
    this.chosedSize.next((event.target as HTMLInputElement).value);
  }

  addToCart(): void{
    this.cartProduct.quantity++;
    this.cartService.addProduct(this.cartProduct);
  }

  addToFavs(): void{
    this.favsService.addProduct(this.product);
  }

  removeFromFavs(): void{
    this.favsService.removeProduct(this.product.id);
  }

  ngOnInit(): void {
    this.chosedSize.next(this.product.sizes[0]);

    this.colors$ = this.productsService.getColors(this.product.name);

    this.chosedSize.subscribe(chosedSize => {
      if (this.product !== undefined){
        const cartProduct: ICartProduct = this.productCartAdapter.getProduct(this.product, chosedSize)

        if (this.cartService.isInCart(cartProduct)){
          this.cartProduct = this.cartService.getProduct(cartProduct);
        }
        else{
          this.cartProduct = this.productCartAdapter.getProduct(this.product, chosedSize);
        }
      }
    })
  }
}
