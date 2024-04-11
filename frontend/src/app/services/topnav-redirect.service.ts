import { TopnavFiltersService } from './topnav-filters.service';
import { TypeDataField } from '../models/filter';
import { FilterService } from './filter.service';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class TopnavRedirectService {
  constructor(
    private filter: FilterService,
    private route: Router,
    private topnavFilterService: TopnavFiltersService,
  ) {
  }

  infoIndex: number = 0;
  openedInfo: boolean = false;

  async goToCatalog(filters?: {brand?: string, category?: TypeDataField}){
    this.filter.globalReset()

    if (this.infoIndex === 3){
      await this.route.navigate(["catalog/zhenskoe"]);
    }
    else if (this.infoIndex === 2){
      await this.route.navigate(["catalog/muzhskoe"]);
    }
    else if (this.infoIndex === 0){
      await this.route.navigate(["catalog/new"]);
    }
    else if (this.infoIndex === 1){
      if (filters === undefined){
        await this.route.navigate(["catalog/new"]);
      }
    }
    else if (this.infoIndex === 4){
      await this.route.navigate(["catalog/accessories"]);
    }
  }

  defaultFilter(filters?: {brand?: string, category?: TypeDataField}){
    this.goToCatalog(filters)
      .then(() => {
        this.closeInfo();

        if (filters !== undefined){
          if (filters.brand){
            this.filter.brandFilters$.next([filters.brand])
            this.filter.brands = [{viewed_name: filters.brand, name: filters.brand}];
          }
          if (filters.category){
            this.filter.categoryFilters$.next([filters.category.name])
            this.topnavFilterService.refs$.next([...this.topnavFilterService.refs$.getValue(), filters.category])
            this.filter.categories = [filters.category];
          }
        }
      })
  }

  openInfo(newInfoIndex?: number){
    this.openedInfo = true;
    if (newInfoIndex != undefined){
      this.infoIndex = newInfoIndex;
    }
    const info = document.getElementById("base");
    if (info != undefined){
      info.style.height = "460px";
      info.style.boxShadow = "0.4em 0.4em 10px rgba(122, 122, 122, 0.5)";
    }
  }

  closeInfo(newInfoIndex?: number){
    this.openedInfo = false;
    if (newInfoIndex != undefined){
      this.infoIndex = newInfoIndex;
    }
    const info = document.getElementById("base");
    if (info != undefined){
      info.style.height = "0px";
      info.style.boxShadow = "none";
    }
  }
}
