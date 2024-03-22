import { HttpClient, HttpHeaders, HttpErrorResponse } from "@angular/common/http";
import { GlobalSettingsService } from "./global-settings.service";
import { Observable, catchError, throwError } from 'rxjs';
import { FilterService } from "./filter.service";
import { ErrorService } from "./error.service";
import { IProduct } from "../models/product";
import { Injectable } from "@angular/core";


@Injectable({
    providedIn: "root"
})
export class ProductsService{
    constructor(
        private http: HttpClient,
        private errorService: ErrorService,
        private filter: FilterService,
        private global: GlobalSettingsService,
    ){
        this.host = this.global.host + 'products';
    }
    host: string;

    httpOptions = {
        headers: new HttpHeaders({
            'accept': 'application/json',
            'Content-Type': 'application/json',
        })
    };

    getProduct(id: number): Observable<IProduct>{
        return this.http.get<IProduct>(this.host + `/product/${id}`).pipe(
            catchError(this.errorHandler.bind(this))
        )
    }

    getColors(name: string): Observable<IProduct[]>{
        return this.http.get<IProduct[]>(this.host + `/product-colors/${name}`).pipe(
            catchError(this.errorHandler.bind(this))
        )
    }

    getSearched(searchBy: string): Observable<IProduct[]>{
        const data = {
            search: searchBy
        }

        return this.http.post<IProduct[]>(this.host + `/search`, data, this.httpOptions).pipe(
            catchError(this.errorHandler.bind(this))
        )
    }

    getFiltered(): Observable<IProduct[]>{
        const data = {
            gender: this.filter.genderFilters$.getValue().join(),
            category: this.filter.categoryFilters$.getValue().join(),
            brand: this.filter.brandFilters$.getValue().join(),
            size: this.filter.sizeFilters$.getValue().join(),
            color: this.filter.colorFilters$.getValue().join(),
            price: this.filter.price$.getValue(),
            quantity: this.filter.quantity$.getValue(),
            pageIndex: this.filter.pageIndex$.getValue(),
            orderBy: this.filter.orderBy$.getValue(),
            basicCategory: this.filter.basicCategory$.getValue(),
        };

        //console.log(data);

        return this.http.post<IProduct[]>(this.host + '/get-filtered', data, this.httpOptions).pipe(
            catchError(this.errorHandler.bind(this))
        )
    }

    getPopularProducts(): Observable<IProduct[]>{
        return this.http.get<IProduct[]>(this.host + '/populars').pipe(
            catchError(this.errorHandler.bind(this))
        )
    }

    getNewArrivals(): Observable<IProduct[]>{
        return this.http.get<IProduct[]>(this.host + '/new-arrivals').pipe(
            catchError(this.errorHandler.bind(this))
        )
    }

    private errorHandler(error: HttpErrorResponse){
        this.errorService.handle(error.message)
        return throwError(() => error.message)
    }
}