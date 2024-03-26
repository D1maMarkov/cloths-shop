import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductPageComponent } from './pages/product-page/product-page.component';
import { CatalogComponent } from './pages/catalog/catalog.component';
import { MainPageComponent } from './pages/main-page/main-page.component';
import { ProfileComponent } from './pages/profile/profile.component';
import { WishlistComponent } from './pages/wishlist/wishlist.component';
import { LoginComponent } from './pages/login/login.component';
import { RegisterComponent } from './pages/register/register.component';
import { OrderComponent } from './pages/order/order.component';
import { AuthGuard } from './guards/auth-guards.guard';
import { NotFoundComponent } from './pages/not-found/not-found.component';
import { ConfirmEmailComponent } from './pages/confirm-email/confirm-email.component';

const routes: Routes = [
  { path: '', component: MainPageComponent},
  { path: 'catalog/:label', component: CatalogComponent},
  { path: 'product/:id', component: ProductPageComponent},
  { path: 'profile', component: ProfileComponent, canActivate: [AuthGuard]},
  { path: 'wishlist', component: WishlistComponent},
  { path: 'login', component: LoginComponent},
  { path: 'register', component: RegisterComponent},
  { path: 'order', component: OrderComponent},
  { path: 'confirm-email/:token', component: ConfirmEmailComponent},
  { path: '404', component: NotFoundComponent},
  { path: '**', redirectTo: '/404'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
