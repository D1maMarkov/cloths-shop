import { HttpClient, HttpHeaders, HttpErrorResponse } from "@angular/common/http";
import { throwError } from 'rxjs';
import { GlobalSettingsService } from "../services/global-settings.service";
import { ErrorService } from "../services/error.service";


export class HttpBaseService{
  host: string;
  http: HttpClient

  httpOptions = {
    withCredentials: true,
    headers: new HttpHeaders({
      'accept': 'application/json',
      'Content-Type': 'application/json',
  })
  };

  constructor(
    http: HttpClient,
    private errorService: ErrorService,
    private global: GlobalSettingsService,
  ){
    this.http = http;
    this.host = this.global.host
  }

  errorHandler(error: HttpErrorResponse){
    this.errorService.handle(error.message)
    return throwError(() => error.message)
  }
}
