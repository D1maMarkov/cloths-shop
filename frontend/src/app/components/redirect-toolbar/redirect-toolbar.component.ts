import { Component, Input, OnInit } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { TopnavFiltersService } from 'src/app/services/topnav-filters.service';
import { TypeDataField } from 'src/app/models/filter';

@Component({
  selector: 'app-redirect-toolbar',
  templateUrl: './redirect-toolbar.component.html',
  styleUrls: ['./redirect-toolbar.component.scss']
})
export class RedirectToolbarComponent implements OnInit {
  defaultRefs: TypeDataField[];

  @Input() refs?: BehaviorSubject<TypeDataField[]>;

  constructor(
    private topnavFilterService: TopnavFiltersService
  ) {
  }

  ngOnInit(): void {
    if (this.refs === undefined){
      this.topnavFilterService.refs$.subscribe(refs => {
        this.defaultRefs = refs;
      })

      this.defaultRefs = this.topnavFilterService.refs$.getValue();
    }
    else {
      this.refs.subscribe(refs => {
        this.defaultRefs = refs;
      })
    };
  }
}
