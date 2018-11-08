import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {globals} from './globals/globals';

const httpOptions = {
headers: new HttpHeaders({
'Content-Type':  'application/json'
}),
responseType: 'text'
};

@Injectable({
  providedIn: 'root'
})
export class BEService {

  constructor(private http:HttpClient) { }

  baseURL = "http://localhost:8000/";

  plotsURL = this.baseURL + 'plots/';
  defineplotsURL = this.baseURL + 'define-plots/';

  postlots(lots){
      return this.http.post(this.plotsURL, lots, {responseType: 'text'});
  }

  getlots(){
      return this.http.get(this.plotsURL, {responseType: 'json'});
  }

  post_define_lots(lots){
      return this.http.post(this.defineplotsURL, { lots: lots}, {responseType: 'text'});
  }
}
