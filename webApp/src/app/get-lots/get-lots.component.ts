import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {BEService} from '../be.service';

@Component({
  selector: 'app-get-lots',
  templateUrl: './get-lots.component.html',
  styleUrls: ['./get-lots.component.css']
})
export class GetLotsComponent implements OnInit {

  lotname = "";
  lots = [];
  constructor(private backend:BEService, private router:Router) {
      
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
          console.log(data);
          this.router.navigateByUrl('/define-lots');
      });
  }


}
