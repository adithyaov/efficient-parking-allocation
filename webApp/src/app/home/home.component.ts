import { Component, OnInit } from '@angular/core';
import {BEService} from '../be.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private backend: BEService, private router:Router) { }
  plots:any = [];
  destinations:any = [];
  parkingdata;
  groups;

  ngOnInit() {
      // this.plots.push({'name': 'PLot 54D', 'lat': 25.36, 'long': 66.321, 'capacity': 12, 'freespace': 5});
      // this.plots.push({'name': 'PLot 54D', 'lat': 25.36, 'long': 66.321, 'capacity': 12, 'freespace': 5});
      // this.destinations.push({'id': 6, 'name': 'mayank'});
      // this.destinations.push({'id': 5, 'name': 'adit'});
      this.backend.getparkinglots_poll().subscribe((data)=>{
        if(data == []){
          this.router.navigateByUrl('/admin');
        }
        this.plots = data;
      });
      this.backend.getbuildings().subscribe((data) =>{
        this.destinations = data;
      })
      this.backend.getgroups().subscribe((data)=>{
        this.groups = data;
      })
      var script = document.createElement('script');
      document.body.appendChild(script)
      // script.onload = this.onMathJaxLoaded.bind(this);
      script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyC6x3DiwoaU4g_Cu_L2Oi-xuGHKwvMLc7E&callback=initMap';
      this.parkingdata = {'p_lot': {'lat': 0, 'long': 0, 'name': ''}, 'dest': {'lat': 0, 'long': 0}, 'parkingspace':{'name': ''}};
  }

  getparking(){
      var dest_id = (<HTMLInputElement>document.getElementById('destination_select')).value;
      var group_id = (<HTMLInputElement>document.getElementById('group_select')).value;
      this.backend.getparkingspace(dest_id, group_id).subscribe((data) =>{
        this.parkingdata = data;
        document.getElementById('resultbox').style.display = 'inline-block';
      },
      (err)=>{
        alert("could not find a parking space");
      });
      console.log(dest_id);
  }

}
