import { HttpClient } from "@angular/common/http";
import { GlobalSettingsService } from "../services/global-settings.service";
import { Observable, catchError } from 'rxjs';
import { ErrorService } from "../services/error.service";
import { IProduct, ICatalogProduct } from "../models/product";
import { Injectable } from "@angular/core";
import { HttpBaseService } from "./base-http-service.service";
import { TypeFilterData } from "../models/filter";

@Injectable({
    providedIn: "root"
})
export class ProductsService extends HttpBaseService{
    constructor(
        http: HttpClient,
        errorService: ErrorService,
        global: GlobalSettingsService,
    ){
        super(http, errorService, global)
        this.host = this.host + 'products';
    }

    getProduct(id: number): Observable<IProduct>{
        return this.http.get<IProduct>(this.host + `/product/${id}`).pipe(
            catchError(this.errorHandler.bind(this))
        )
    }

    getColors(name: string): Observable<ICatalogProduct[]>{
        return this.http.get<ICatalogProduct[]>(this.host + `/product-colors/${name}`).pipe(
            catchError(this.errorHandler.bind(this))
        )
    }

    getSearched(searchBy: string): Observable<ICatalogProduct[]>{
        const data = {
            search: searchBy
        }

        return this.http.post<ICatalogProduct[]>(this.host + `/search`, data, this.httpOptions).pipe(
            catchError(this.errorHandler.bind(this))
        )
    }

    getFiltered(data: TypeFilterData): Observable<ICatalogProduct[]>{
        return this.http.post<ICatalogProduct[]>(this.host + '/get-filtered', data, this.httpOptions).pipe(
            catchError(this.errorHandler.bind(this))
        )
    }

    getPopularProducts(): Observable<ICatalogProduct[]>{
        return this.http.get<ICatalogProduct[]>(this.host + '/populars').pipe(
            catchError(this.errorHandler.bind(this))
        )
    }

    getNewArrivals(): Observable<ICatalogProduct[]>{
        return this.http.get<ICatalogProduct[]>(this.host + '/new-arrivals').pipe(
            catchError(this.errorHandler.bind(this))
        )
    }
}
