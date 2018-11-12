import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {globals} from './globals/globals';
import { of } from 'rxjs/observable/of'

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
  // baseURL = "/";

  getadminURL = this.baseURL + 'get/setup/';
  plotsURL = this.baseURL + 'plots/';
  defineplotsURL = this.baseURL + 'define-plots/';
  buildingsURL = this.baseURL + 'buildings/';
  interconnectsURL = this.baseURL + 'interconnects/';
  cameraguideURL = this.baseURL + 'camera-guide/';
  getpspacenameURL = this.baseURL + 'get/pspaces';
  getpspaceimageURL = this.baseURL + 'get/pspaceimage'
  postpspacenameURL = this.baseURL + 'post/pspaces';

  postlots(lots){
      return this.http.post(this.plotsURL, lots, {responseType: 'text'});
  }

  getlots(){
      return this.http.get(this.plotsURL, {responseType: 'json'});
  }

  post_define_lots(lots){
    // var fdata = new FormData();
    // var len = lots.length;
    // for(var i = 0; i < len; i++){
    //   fdata.append('image' + i, lots[i].image);
    // }
    // fdata.append('textdata', JSON.stringify(lots));
      // return this.http.post(this.defineplotsURL, fdata, {responseType: 'text'});
      return this.http.post(this.defineplotsURL, lots, {responseType: 'text'});
  }

  postbuildings(buildings){
      return this.http.post(this.buildingsURL, buildings, {responseType: 'text'});
  }

  getbuildings(){
    return this.http.get(this.buildingsURL, {responseType: 'json'});
  }

  postinterconnects(interconnects){
    return this.http.post(this.interconnectsURL, interconnects, {responseType: 'text'});
  }

  getcameraguide(image, scale){
    var fdata = new FormData();
    fdata.append('image', image);
    fdata.append('scale', scale);
    return of(image);
    // return this.http.post(this.cameraguideURL, fdata, {responseType: 'blob'});
  }

  getpspacenames(id){
    return this.http.get(this.getpspacenameURL + '?id=' + id, {responseType: 'json'});
  }

  getpspaceimage(id){
    return this.http.get(this.getpspaceimageURL + '?id=' + id, {responseType: 'blob'});
  }

  postpspacenames(pspaces){
    return this.http.post(this.postpspacenameURL, pspaces, {responseType: 'text'});
  }
}
