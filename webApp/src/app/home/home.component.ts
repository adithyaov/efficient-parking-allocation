import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor() { }
  plots = [];
  destinations = [];

  ngOnInit() {
      this.plots.push({'name': 'PLot 54D', 'lat': 25.36, 'long': 66.321, 'capacity': 12, 'freespace': 5});
      this.plots.push({'name': 'PLot 54D', 'lat': 25.36, 'long': 66.321, 'capacity': 12, 'freespace': 5});
      this.destinations.push({'id': 6, 'name': 'mayank'});
      this.destinations.push({'id': 5, 'name': 'adit'});
  }

  getparking(){
      var dest_id = (<HTMLInputElement>document.getElementById('destination_select')).value;
      console.log(dest_id);
  }

}
