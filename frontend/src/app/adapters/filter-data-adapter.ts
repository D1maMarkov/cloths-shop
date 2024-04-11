import { FilterService } from "../services/filter.service";
import { TypeFilterData } from "../models/filter";
import { Injectable } from '@angular/core';


@Injectable({
  providedIn: 'root'
})
export class FilterDataAdapter{
    getData(filter: FilterService): TypeFilterData{
        return {
            gender: filter.genderFilters$.getValue(),
            category: filter.categoryFilters$.getValue(),
            brand: filter.brandFilters$.getValue(),
            size: filter.sizeFilters$.getValue(),
            color: filter.colorFilters$.getValue(),
            price: filter.price$.getValue(),
            quantity: filter.quantity$.getValue(),
            pageIndex: filter.pageIndex$.getValue(),
            orderBy: filter.orderBy$.getValue(),
            basicCategory: filter.basicCategory$.getValue(),
        };
    }
}
