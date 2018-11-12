import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {BEService} from '../be.service';

@Component({
  selector: 'app-buildings',
  templateUrl: './buildings.component.html',
  styleUrls: ['./buildings.component.css']
})
export class BuildingsComponent implements OnInit {

  building_name = "";
  buildings = [{'name': '', 'latitude': 0, 'longitude': 0}];
  constructor(private backend:BEService, private router:Router) { }

  ngOnInit() {
  }

  addrow(){
      this.buildings.push({'name': '', 'latitude': 0, 'longitude': 0})
  }

  finish(){
      console.log(this.buildings);
      this.backend.postbuildings(this.buildings).subscribe((data:string) => {
          console.log(data);
          this.router.navigateByUrl('/interconnects');
      });
  }

}
