import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from "@angular/platform-browser/animations"
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProductComponent } from './components/product/product.component';
import { HttpClientModule } from '@angular/common/http';
import { GlobalErrorComponent } from './components/global-error/global-error.component';
import { FormsModule } from '@angular/forms';
import { MainFilterComponent } from './components/main-filter/main-filter.component';
import { SearchProductsPipe } from './pipes/search-products.pipe';
import { Subject } from 'rxjs';
import { TopnavFiltersComponent } from './components/topnav-filters/topnav-filters.component';
import { NgxPaginationModule } from 'ngx-pagination';
import { SearchFilterComponent } from './components/search-filter/search-filter.component';
import { TopnavComponent } from './components/topnav/topnav.component';
import { UnderlinedTextComponent } from './components/underlined-text/underlined-text.component';
import { FooterComponent } from './components/footer/footer.component';
import { ProductPageComponent } from './pages/product-page/product-page.component';
import { RedirectToolbarComponent } from './components/redirect-toolbar/redirect-toolbar.component';
import { CatalogComponent } from './pages/catalog/catalog.component';
import { IsVisibleDirective } from './directives/is-visible.directive';
import { MainPageComponent } from './pages/main-page/main-page.component';
import { PaginateComponent } from './components/paginate-component/paginate-component.component';
import { PaginateBrands } from './components/paginate-brands/paginate-brands.component';
import { ProfileComponent } from './pages/profile/profile.component';
import { Title } from '@angular/platform-browser';
import { ClipboardModule } from '@angular/cdk/clipboard';
import { CopyTextDirective } from './directives/copy-text.directive';
import { CartComponent } from './components/cart/cart.component';
import { MatBadgeModule } from '@angular/material/badge';
import { SearchComponent } from './components/search/search.component';
import { WishlistComponent } from './pages/wishlist/wishlist.component';
import { LoginComponent } from './pages/login/login.component';
import { SimpleTopnavComponent } from './components/simple-topnav/simple-topnav.component';
import { RegisterComponent } from './pages/register/register.component'
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { OrderComponent } from './pages/order/order.component';
import { ReactiveFormsModule } from '@angular/forms';
import { NgxMaskModule } from 'ngx-mask';
import { NotFoundComponent } from './pages/not-found/not-found.component';
import { CartProductComponent } from './components/cart-product/cart-product.component';

@NgModule({
  declarations: [
    AppComponent,
    ProductComponent,
    GlobalErrorComponent,
    MainFilterComponent,
    SearchProductsPipe,
    TopnavFiltersComponent,
    SearchFilterComponent,
    TopnavComponent,
    UnderlinedTextComponent,
    FooterComponent,
    ProductPageComponent,
    RedirectToolbarComponent,
    CatalogComponent,
    IsVisibleDirective,
    MainPageComponent,
    PaginateComponent,
    PaginateBrands,
    ProfileComponent,
    CopyTextDirective,
    CartComponent,
    SearchComponent,
    WishlistComponent,
    LoginComponent,
    SimpleTopnavComponent,
    RegisterComponent,
    OrderComponent,
    NotFoundComponent,
    CartProductComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    BrowserAnimationsModule,
    NgxPaginationModule,
    ClipboardModule,
    MatBadgeModule,
    MatSnackBarModule,
    ReactiveFormsModule,
    NgxMaskModule,
    NgxMaskModule.forRoot()
  ],
  providers: [
    Subject,
    Title
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }