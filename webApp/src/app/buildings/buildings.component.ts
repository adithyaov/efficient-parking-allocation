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
  buildings = [{'name': 'NEC', 'lat': 1.3172116, 'long': 103.8631046}];
  constructor(private backend:BEService, private router:Router) { }

  ngOnInit() {
  }

  addrow(){
      this.buildings.push({'name': '', 'lat': 0, 'long': 0})
  }

  finish(){
      console.log(this.buildings);
      this.backend.postbuildings(this.buildings).subscribe((data:string) => {
          console.log(data);
          this.router.navigateByUrl('/interconnects');
      });
  }

}
