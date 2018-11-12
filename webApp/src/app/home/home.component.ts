import { Component, OnInit } from '@angular/core';
import {BEService} from '../be.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private backend: BEService) { }
  plots = [];
  destinations = [];
  parkingdata;
  groups;

  ngOnInit() {
      // this.plots.push({'name': 'PLot 54D', 'lat': 25.36, 'long': 66.321, 'capacity': 12, 'freespace': 5});
      // this.plots.push({'name': 'PLot 54D', 'lat': 25.36, 'long': 66.321, 'capacity': 12, 'freespace': 5});
      // this.destinations.push({'id': 6, 'name': 'mayank'});
      // this.destinations.push({'id': 5, 'name': 'adit'});
      this.backend.getgroups().subscribe((data)=>{
        this.groups = data;
      })
      var script = document.createElement('script');
      document.body.appendChild(script)
      // script.onload = this.onMathJaxLoaded.bind(this);
      script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyC6x3DiwoaU4g_Cu_L2Oi-xuGHKwvMLc7E&callback=initMap';
      this.parkingdata = {'p_lot': {'lat': 0, 'long': 0}, 'dest': {'lat': 0, 'long': 0}};
  }

  getparking(){
      var dest_id = (<HTMLInputElement>document.getElementById('destination_select')).value;
      var group_id = (<HTMLInputElement>document.getElementById('group_select')).value;
      this.backend.getparkingspace(dest_id, group_id).subscribe((data) =>{
        this.parkingdata = data;
      })
      console.log(dest_id);
  }

}
