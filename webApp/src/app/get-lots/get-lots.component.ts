import { Component, OnInit } from '@angular/core';
import {BEService} from '../be.service';

@Component({
  selector: 'app-get-lots',
  templateUrl: './get-lots.component.html',
  styleUrls: ['./get-lots.component.css']
})
export class GetLotsComponent implements OnInit {

  lotname = "";
  lots = [];
  constructor(private backend:BEService) {
      
   }
  

  ngOnInit() {
  }

  addLot(){
      if(this.lotname!=""){
          this.lots.push(this.lotname);
          this.lotname = "";
      }
  }

  finish(){
      console.log(this.lots);
      this.backend.postlots(this.lots).subscribe((data:string) => {
          console.log("--");
          console.log(data);
      });
  }


}
