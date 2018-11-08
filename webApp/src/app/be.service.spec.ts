import { TestBed } from '@angular/core/testing';

import { BEService } from './be.service';

describe('BEService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: BEService = TestBed.get(BEService);
    expect(service).toBeTruthy();
  });
});
