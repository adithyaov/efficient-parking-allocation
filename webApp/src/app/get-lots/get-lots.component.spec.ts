import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GetLotsComponent } from './get-lots.component';

describe('GetLotsComponent', () => {
  let component: GetLotsComponent;
  let fixture: ComponentFixture<GetLotsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GetLotsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GetLotsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
