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

  postlotsURL = this.baseURL + 'postlots/';

  postlots(lots){
      return this.http.post(this.postlotsURL, lots, {responseType: 'text'});
  }
}
