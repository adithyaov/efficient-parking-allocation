import { Component, OnInit } from '@angular/core';
import {PLot} from '../globals/plot';
import {BEService} from '../be.service';

@Component({
  selector: 'app-define-lots',
  templateUrl: './define-lots.component.html',
  styleUrls: ['./define-lots.component.css']
})
export class DefineLotsComponent implements OnInit {

  constructor(private backend: BEService) { }
  lots;
  baseURL = this.backend.baseURL;

  ngOnInit() {
      this.backend.getlots().subscribe((data)=> {
          this.lots = data;
      })
  }

  finish(){
      this.backend.post_define_lots(this.lots).subscribe((data) =>{
          console.log(data);
      })
  }

}
