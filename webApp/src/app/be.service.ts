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

  baseURL = "http://localhost:8080/";
  // baseURL = "/";

  getadminURL = this.baseURL + 'get/setup';
  getplotsURL = this.baseURL + 'get/lots';
  postplotsURL = this.baseURL + 'post/lots';
  postdefineplotsURL = this.baseURL + 'post/lots';
  postbuildingsURL = this.baseURL + 'post/destinations';
  getbuildingsURL = this.baseURL + 'get/destinations';
  getinterconnectsURL = this.baseURL + 'get/interconnects';
  postinterconnectsURL = this.baseURL + 'post/interconnects';
  cameraguideURL = this.baseURL + 'camera-guide';
  getpspacenameURL = this.baseURL + 'get/probe-ids-init';
  getpspaceimageURL = this.baseURL + 'get/probe-image-init'
  postpspacenameURL = this.baseURL + 'post/pspaces';

  getparkingspaceURL = this.baseURL + 'get/parkingspace';
  getgroupsURL = this.baseURL + 'get/groups';

  postlots(lots){
      return this.http.post(this.postplotsURL, lots, {responseType: 'text'});
  }

  getlots(){
      return this.http.get(this.getplotsURL, {responseType: 'json'});
  }

  post_define_lots(lots){
    // var fdata = new FormData();
    // var len = lots.length;
    // for(var i = 0; i < len; i++){
    //   fdata.append('image' + i, lots[i].image);
    // }
    // fdata.append('textdata', JSON.stringify(lots));
      // return this.http.post(this.defineplotsURL, fdata, {responseType: 'text'});
      return this.http.post(this.postdefineplotsURL, lots, {responseType: 'text'});
  }

  postbuildings(buildings){
      return this.http.post(this.postbuildingsURL, buildings, {responseType: 'text'});
  }

  getbuildings(){
    return this.http.get(this.getbuildingsURL, {responseType: 'json'});
  }

  getinterconnects(){
    return this.http.get(this.getinterconnectsURL, {responseType: 'json'});
  }

  postinterconnects(interconnects){
    return this.http.post(this.postinterconnectsURL, interconnects, {responseType: 'text'});
  }

  getcameraguide(image, scale){
    var fdata = new FormData();
    fdata.append('image', image);
    fdata.append('scale', scale);
    return of(image);
    // return this.http.post(this.cameraguideURL, fdata, {responseType: 'blob'});
  }

  getpspacenames(id){
    return this.http.get(this.getpspacenameURL + '/' + id, {responseType: 'json'});
  }

  getpspaceimage(id){
    return this.http.get(this.getpspaceimageURL + '/' + id, {responseType: 'blob'});
  }

  postpspacenames(pspaces){
    return this.http.post(this.postpspacenameURL, pspaces, {responseType: 'text'});
  }

  getparkingspace(dest_id, group_id){
    return this.http.get(this.getparkingspaceURL + '/' + dest_id + '/' + group_id, {responseType: 'json'});
  }

  getgroups(){
    return this.http.get(this.getgroupsURL, {responseType: 'json'});
  }
}
