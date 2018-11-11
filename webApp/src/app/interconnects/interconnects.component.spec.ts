import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InterconnectsComponent } from './interconnects.component';

describe('InterconnectsComponent', () => {
  let component: InterconnectsComponent;
  let fixture: ComponentFixture<InterconnectsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InterconnectsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InterconnectsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
