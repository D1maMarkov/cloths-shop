import { IsVisibleImageService } from 'src/app/services/is-visible-image.service';
import { ProductsService } from 'src/app/services/products.service';
import { IProduct, TypeCartProduct } from 'src/app/models/product';
import { SearchService } from 'src/app/services/search.service';
import { fadeIn } from 'src/app/animations/fade-in.animation';
import { CartService } from 'src/app/services/cart.service';
import { FavsService } from 'src/app/services/favs.service';
import { TypeDataFilter } from 'src/app/models/filter';
import { BehaviorSubject, Observable } from 'rxjs';
import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: 'app-product-page',
  templateUrl: './product-page.component.html',
  styleUrls: ['./product-page.component.scss'],
  animations: [fadeIn]
})
export class ProductPageComponent implements OnInit {
  colors$: Observable<IProduct[]>;

  refs = new BehaviorSubject<TypeDataFilter[]>([
    {
      viewed_name: "Новинки", 
      name: 'unisex'
    }
  ]);

  product: IProduct;
  products$: Observable<IProduct[]>;

  chosedSize = new BehaviorSubject<string>('');

  visibleImageId: number;

  isInFavs = new BehaviorSubject<boolean>(false);
  cartProduct: TypeCartProduct;

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

  constructor(
    private productsService: ProductsService, 
    private route: ActivatedRoute, 
    private visibleService: IsVisibleImageService,
    private titleService: Title,
    public cartService: CartService,
    public favsService: FavsService,
    private searchService: SearchService,
  ){
    this.searchService.opened = false;
    this.products$ = this.productsService.getSearched("");
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const id = params['id']; 
     
      this.productsService.getProduct(id).subscribe(product => {
        this.product = product;

        this.chosedSize.next(product.sizes[0]);

        this.refs.next([...this.refs.getValue(), {name: product.category.name, viewed_name: product.category.viewed_name}]); 
        this.refs.next([...this.refs.getValue(), {name: product.name, viewed_name: product.name}]);
        
        this.titleService.setTitle(product.name);
        this.colors$ = this.productsService.getColors(product.name);
      })
    });

    this.visibleService.visibleImageId$.subscribe(id => {
      this.visibleImageId = id;
    })

    this.chosedSize.subscribe(chosedSize => {
      if (this.product !== undefined){

        const cartProduct: TypeCartProduct = {
          id: this.product.id,
          name: this.product.name,
          description: this.product.description,
          price: this.product.price,
          size: chosedSize,
          quantity: 0,
          image: this.product.images[0]
        }

        if (this.cartService.isInCart(cartProduct)){
          this.cartProduct = this.cartService.getProduct(cartProduct);
        }
        else{
          this.cartProduct = cartProduct;
        }
      }
    })
  }
}