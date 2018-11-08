import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-get-lots',
  templateUrl: './get-lots.component.html',
  styleUrls: ['./get-lots.component.css']
})
export class GetLotsComponent implements OnInit {

  lotname = "";
  lots = [];
  constructor() {
      
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
  }


}
