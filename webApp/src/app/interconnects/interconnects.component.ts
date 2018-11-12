import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {BEService} from '../be.service';

@Component({
  selector: 'app-interconnects',
  templateUrl: './interconnects.component.html',
  styleUrls: ['./interconnects.component.css']
})
export class InterconnectsComponent implements OnInit {

  constructor(private backend: BEService, private router:Router) { }
  lots = [];
  buildings = [];
  interconnects = {};

  ngOnInit() {
      this.backend.getlots().subscribe((data: any[])=> {
          this.lots = data;
          this.backend.getbuildings().subscribe((data: any[]) => {
              this.buildings = data;
              this.buildings.forEach((b) => {
                  var s = {};
                  this.lots.forEach((l) =>{
                      s[l.id] = 0;
                  })
                  this.interconnects[b.id] = s;
              })
              this.backend.getinterconnects().subscribe((idata: any[])=>{
                idata.forEach((i) =>{
                  this.interconnects[i['destination_id']][i['p_lot_id']] = i['distance'];
                })
              })
          })
      }) 
  }

  finish(){
      console.log(this.interconnects);
      this.backend.postinterconnects(this.interconnects).subscribe((data:string) => {
          console.log(data);
          // this.router.navigateByUrl('/define-lots');
      });
  }
}
