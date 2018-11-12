import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {BEService} from '../be.service';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent implements OnInit {

  constructor(private backend:BEService, private router:Router) { }

  steps = ['PLots', 'Buildings', 'Interconnects', 'PSpaces'];

  states = {
      'PLots': {'name': 'Define Parking Lots', 'finished': false, 'link': '/define-lots'},
      'Buildings': {'name': 'Define Buildings', 'finished': false, 'link': '/buildings'},
      'Interconnects': {'name': 'Define Interconnects', 'finished': false, 'link': '/interconnects'},
      'PSpaces': {'name': 'Define Parking Spaces', 'finished': false, 'link': '/define-pspace'},
  }

  ngOnInit() {
  }

  finish(){
      this.router.navigateByUrl('/define-lots');
  }

}
